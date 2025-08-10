import { Routes, Route } from 'react-router-dom';
import Home from './Pages/home';
import { useEffect, useRef } from 'react';

export default function App() {
  useEffect(() => {
    window.enviarResultado = function(name, score, time) {
      console.log("Função window.enviarResultado chamada com:", { name, score, time });

      fetch('https://api-ets.vercel.app/api/ranking', {  // Note o "/api" para Vercel
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, score, time }),
      })
        .then((res) => {
          console.log("Resposta do servidor:", res.status);
          if (!res.ok) throw new Error('Erro ao enviar resultado');
          return res.json();
        })
        .then((data) => {
          console.log('Resultado enviado com sucesso:', data);
        })
        .catch((err) => {
          console.error('Falha no envio:', err);
        });
    };
  }, []);

  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
}
