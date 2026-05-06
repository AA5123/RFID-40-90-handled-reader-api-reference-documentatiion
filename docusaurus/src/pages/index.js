import React, { useEffect } from "react";
import useBaseUrl from "@docusaurus/useBaseUrl";

export default function Home() {
  const docsUrl = useBaseUrl("/docs/");

  useEffect(function () {
    window.location.replace(docsUrl);
  }, [docsUrl]);

  return (
    <main style={{ padding: "2rem", fontFamily: "system-ui, sans-serif" }}>
      <p>Redirecting to API reference...</p>
      <p>
        If you are not redirected, open <a href={docsUrl}>the API reference page</a>.
      </p>
    </main>
  );
}
