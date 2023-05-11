import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import Home from "./components/screens/Home/Home.tsx";
import Layout from "./components/layout/Layout.tsx";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <Layout>
      <Home />
    </Layout>
  </React.StrictMode>
);
