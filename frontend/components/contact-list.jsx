"use client";

import React from "react";

import useSWRInfinite from "swr/infinite";

import { fetcher } from "@/app/lib/api";

import ContactDetails from "@/components/contact-details";

import {
  Accordion,
  AccordionItem,
  Avatar,
  AvatarIcon,
} from "@nextui-org/react";
import { Spinner } from "@nextui-org/react";
import { useInView } from "react-intersection-observer";
import { useEffect } from "react";

export const getKey = (pageIndex, previousPageData) => {
  if (previousPageData && !previousPageData.length) return null;
  var path = `/contacts/?skip=${pageIndex * process.env.NEXT_PUBLIC_PAGE_SIZE}&limit=${process.env.NEXT_PUBLIC_PAGE_SIZE}`;
  return path;
};

export default function ContactList() {
  const { data, size, setSize, error, isLoading } = useSWRInfinite(
    getKey,
    fetcher,
  );
  const { ref, inView } = useInView();

  const isEmpty = data?.[0]?.length === 0;
  const isReachingEnd =
    isEmpty ||
    (data && data[data.length - 1]?.length < process.env.NEXT_PUBLIC_PAGE_SIZE);

  useEffect(() => {
    if (inView && !isReachingEnd) {
      setSize(size + 1);
    }
  }, [inView, isReachingEnd, setSize, size]);

  if (error) return <div>Error</div>;
  if (isLoading) return <Spinner className="flex justify-center h-max" />;

  return (
    <>
      <Accordion selectionMode="multiple">
        {data.map((contacts, index) => {
          return contacts.map((contact) => (
            <AccordionItem
              key={contact.id}
              startContent={
                <Avatar
                  name={contact.first_name.charAt(0).toUpperCase()}
                  icon={<AvatarIcon />}
                />
              }
              aria-label={`${contact.first_name} ${contact.last_name}`}
              title={`${contact.first_name} ${contact.last_name}`}
            >
              <ContactDetails contactId={contact.id} />
            </AccordionItem>
          ));
        })}
      </Accordion>
      <div ref={ref} className="flex justify-center">
        {!isReachingEnd ? (
          <Spinner size="lg" className="self-center" />
        ) : (
          <p>{isEmpty ? "No contacts." : "No more contacts."}</p>
        )}
      </div>
    </>
  );
}
