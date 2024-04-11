import ContactList from "@/components/contact-list";
import FloatingButton from "@/components/floating-button";

export default function Home() {
  return (
    <div className="flex justify-center">
      <div className="max-w-6xl w-full">
        <ContactList />
      </div>
      <FloatingButton />
    </div>
  );
}
