export const fetcher = (path) =>
  fetch(`${process.env.NEXT_PUBLIC_BACKEND_API_URL}${path}`).then((r) =>
    r.json(),
  );

export async function createContact(contactCreate) {
  return fetch(`${process.env.NEXT_PUBLIC_BACKEND_API_URL}/contacts/`, {
    method: "POST",
    body: JSON.stringify(contactCreate),
  }).then((r) => r.json());
}
