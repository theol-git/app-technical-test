"use client";

import React from "react";
import { fetcher } from "@/app/lib/api";
import useSWR from "swr";
import { Listbox, ListboxItem } from "@nextui-org/react";
import { ListboxWrapper } from "@/components/listbox-wrapper";
import {
  Briefcase as JobIcon,
  MapPin as AddressIcon,
  QuestionCircle as QuestionIcon,
} from "@geist-ui/icons";

export default function ContactDetails({ contactId: contactId }) {
  const {
    data: contact,
    error,
    isLoading,
  } = useSWR(`/contacts/${contactId}`, fetcher);

  if (error) return <div>Error</div>;
  if (isLoading) return <div>IsLoading</div>;
  if (!contact || (!contact.question && !contact.job && !contact.address))
    return <div />;

  const iconClasses =
    "text-xl text-default-500 pointer-events-none flex-shrink-0";

  const listItems = [
    contact.job && {
      key: "job",
      value: contact.job,
      icon: <JobIcon className={iconClasses} />,
    },
    contact.address && {
      key: "address",
      value: contact.address,
      icon: <AddressIcon className={iconClasses} />,
    },
    contact.question && {
      key: "question",
      value: contact.question,
      icon: <QuestionIcon className={iconClasses} />,
    },
  ].filter(Boolean);

  return (
    <ListboxWrapper>
      <Listbox items={listItems} variant="faded" aria-label="Contact info">
        {(item) => (
          <ListboxItem key={item.key} startContent={item.icon}>
            {item.value}
          </ListboxItem>
        )}
      </Listbox>
    </ListboxWrapper>
  );
}
