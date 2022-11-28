import { BrowserRouter, Routes, Route } from "react-router-dom";
import NotFound404 from "./pages/error_page/NotFound404";
import LandingPage from "./pages/landing_page/LandingPage";


const Router = () => {
    return <BrowserRouter>
        <Routes>
            <Route path='/' element={<LandingPage />} />
            <Route element={<NotFound404 />} />
        </Routes>
    </BrowserRouter>
}

export default Router;