"use client";

import { toast } from "sonner";
import { Button } from "@/components/ui/button";

export function CopyLinkButton({
  url,
  label,
  copiedLabel,
}: {
  url: string;
  label: string;
  copiedLabel: string;
}) {
  return (
    <Button
      type="button"
      variant="secondary"
      onClick={async () => {
        await navigator.clipboard.writeText(url);
        toast.success(copiedLabel);
      }}
    >
      {label}
    </Button>
  );
}
