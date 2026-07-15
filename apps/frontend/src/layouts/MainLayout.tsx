import Sidebar from "../components/layout/Sidebar";
import Header from "../components/layout/Header";
import StatusBar from "../components/layout/StatusBar";

import "./MainLayout.css";

interface Props {
  children: React.ReactNode;
}

export default function MainLayout({ children }: Props) {
  return (
    <div className="app">

      <Sidebar />

      <div className="workspace">

        <Header />

        <main className="content">
          {children}
        </main>

        <StatusBar />

      </div>

    </div>
  );
}