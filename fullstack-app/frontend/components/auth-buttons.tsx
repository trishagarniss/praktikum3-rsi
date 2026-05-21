"use client";

import { useSyncExternalStore } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";

function getSnapshot() {
  if (typeof window === "undefined") return true;
  return !localStorage.getItem("token");
}

function subscribe(cb: () => void) {
  window.addEventListener("storage", cb);
  window.addEventListener("auth-change", cb);
  return () => {
    window.removeEventListener("storage", cb);
    window.removeEventListener("auth-change", cb);
  };
}

export function AuthButtons() {
  const show = useSyncExternalStore(subscribe, getSnapshot, () => true);

  if (!show) return null;

  return (
    <div className="flex gap-3">
      <Button asChild>
        <Link href="/auth/register">Daftar Sekarang</Link>
      </Button>
      <Button variant="outline" asChild>
        <Link href="/auth/login">Masuk</Link>
      </Button>
    </div>
  );
}
