import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Login } from "../paginas/Login";
import { Inicial } from "../paginas/Inicial";
// import { Reserva } from "../paginas/Reserva";

export function Rotas() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/inicial" element={<Inicial />} >
            {/* <Route index element={<Reserva />} /> */}
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
