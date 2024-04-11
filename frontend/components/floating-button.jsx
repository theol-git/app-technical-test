"use client";

import React, { useEffect } from "react";

import { Plus } from "@geist-ui/icons";
import { useSWRConfig } from "swr";
import { unstable_serialize } from "swr/infinite";

import {
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Button,
  useDisclosure,
  Input,
} from "@nextui-org/react";
import { useForm } from "react-hook-form";
import { createContact } from "@/app/lib/api";
import { getKey } from "@/components/contact-list";

export default function FloatingButton() {
  const { isOpen, onOpen, onOpenChange } = useDisclosure();
  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, isSubmitted, isSubmitSuccessful },
  } = useForm();

  const { mutate } = useSWRConfig();

  const reloadContacts = async (contact) => {
    mutate(unstable_serialize(getKey), async (contactPages) => {
      if (
        contactPages.length == 0 ||
        contactPages[contactPages.length - 1].length >=
          process.env.NEXT_PUBLIC_PAGE_SIZE
      ) {
        contactPages.push([]);
      }
      contactPages[contactPages.length - 1].push([
        {
          id: contact.id,
          first_name: contact.first_name,
          last_name: contact.last_name,
        },
      ]);
    });
  };

  const onSave = async (data) => {
    const contact = await createContact(data);
    reloadContacts(contact);
  };

  useEffect(() => {
    setTimeout(() => {
      reset(undefined, { keepIsSuccessful: false });
    }, 2000);
  }, [reset]);

  return (
    <>
      <div className="fixed bottom-0 w-full">
        <Button
          onPress={onOpen}
          size="lg"
          className="float-right my-8 mx-8"
          color="primary"
          variant="shadow"
          startContent={<Plus />}
        >
          Create Contact
        </Button>
      </div>

      <Modal isOpen={isOpen} onOpenChange={onOpenChange} placement="top-center">
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                New Contact
              </ModalHeader>
              <ModalBody>
                <form id="new-contact" onSubmit={handleSubmit(onSave)}>
                  <Input
                    autoFocus
                    isRequired
                    label="First Name"
                    placeholder="Bob"
                    variant="bordered"
                    {...register("first_name")}
                  />

                  <Input
                    isRequired
                    label="Last Name"
                    placeholder="Ross"
                    variant="bordered"
                    {...register("last_name")}
                  />

                  <Input
                    label="Job"
                    placeholder="Plumber"
                    variant="bordered"
                    {...register("job")}
                  />

                  <Input
                    label="Address"
                    placeholder="Champ de Mars, 5 Av. Anatole France, 75007 Paris"
                    variant="bordered"
                    {...register("address")}
                  />

                  <Input
                    label="Question"
                    placeholder="What time is it?"
                    variant="bordered"
                    {...register("question")}
                  />
                </form>
              </ModalBody>

              <ModalFooter>
                <Button color="danger" variant="flat" onPress={onClose}>
                  Close
                </Button>
                <Button
                  color={isSubmitted ? "success" : "primary"}
                  form="new-contact"
                  type="submit"
                >
                  {isSubmitted ? "Saved" : isSubmitting ? "Saving..." : "Save"}
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
}
