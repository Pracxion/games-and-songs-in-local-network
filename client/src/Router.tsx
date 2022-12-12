import { BrowserRouter, Routes, Route } from "react-router-dom";
import NotFound404 from "./pages/error_page/NotFound404";
import { LandingPage } from "./pages/landing_page/LandingPage";
import HubPage from "./pages/main_hub/HubPage";


const Router = () => {
    return <BrowserRouter>
        <Routes>
            <Route path='/' element={<LandingPage />} />
            <Route path='/@me' element={<HubPage />} />
            <Route element={<NotFound404 />} />
        </Routes>
    </BrowserRouter>
}

export default Router;