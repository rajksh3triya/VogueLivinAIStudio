import { Link, useLocation } from "react-router-dom";

const menu = [
  { name: "Dashboard", path: "/" },
  { name: "Projects", path: "/projects" },
  { name: "Scenes", path: "/scenes" },
  { name: "Camera", path: "/camera" },
  { name: "Queue", path: "/queue" },
  { name: "Models", path: "/models" },
  { name: "Settings", path: "/settings" },
];

export default function Sidebar() {
  const location = useLocation();

  return (
    <aside className="sidebar">
      <div className="logo">VogueLivin AI</div>

      {menu.map((item) => (
        <Link
          key={item.path}
          to={item.path}
          className={
            location.pathname === item.path
              ? "menu-item active"
              : "menu-item"
          }
        >
          {item.name}
        </Link>
      ))}
    </aside>
  );
}