import { Routes, Route, Navigate } from "react-router-dom";

import Dashboard from "../pages/Dashboard";
import Projects from "../pages/Projects";
import Scenes from "../pages/Scenes";
import Camera from "../pages/Camera";
import Queue from "../pages/Queue";
import Models from "../pages/Models";
import Settings from "../pages/Settings";

import MainLayout from "../layouts/MainLayout";

export default function AppRouter() {
  return (
    <Routes>

      <Route
        path="/"
        element={
          <MainLayout>
            <Dashboard />
          </MainLayout>
        }
      />

      <Route
        path="/projects"
        element={
          <MainLayout>
            <Projects />
          </MainLayout>
        }
      />

      <Route
        path="/scenes"
        element={
          <MainLayout>
            <Scenes />
          </MainLayout>
        }
      />

      <Route
        path="/camera"
        element={
          <MainLayout>
            <Camera />
          </MainLayout>
        }
      />

      <Route
        path="/queue"
        element={
          <MainLayout>
            <Queue />
          </MainLayout>
        }
      />

      <Route
        path="/models"
        element={
          <MainLayout>
            <Models />
          </MainLayout>
        }
      />

      <Route
        path="/settings"
        element={
          <MainLayout>
            <Settings />
          </MainLayout>
        }
      />

      <Route path="*" element={<Navigate to="/" replace />} />

    </Routes>
  );
}