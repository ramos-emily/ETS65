import { useRef, useEffect, useState } from "react";

const API_URL = "https://ranking-api.vercel.app";

export async function enviarResultado(nome, pontos, tempo) {
  try {
    const res = await fetch(`${API_URL}/ranking`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: nome, score: pontos, time: tempo }),
    });
    if (!res.ok) throw new Error("Erro ao enviar resultado");
    const data = await res.json();
    console.log("Resultado enviado:", data);
  } catch (err) {
    console.error(err);
  }
}

export default function Home() {
  const iframeRef = useRef(null);
  const [dimensions, setDimensions] = useState({ 
    width: window.innerWidth, 
    height: window.innerHeight 
  });

  useEffect(() => {
    // Entrar em tela cheia automaticamente quando o componente montar
    const enterFullscreen = () => {
      const element = document.documentElement;
      if (element.requestFullscreen) {
        element.requestFullscreen().catch(err => {
          console.log('Erro ao tentar tela cheia automática:', err);
        });
      } else if (element.webkitRequestFullscreen) { // Safari
        element.webkitRequestFullscreen();
      } else if (element.msRequestFullscreen) { // IE11
        element.msRequestFullscreen();
      }
    };

    // Tentar entrar em tela cheia automaticamente
    enterFullscreen();

    function handleResize() {
      setDimensions({
        width: window.innerWidth,
        height: window.innerHeight
      });
    }

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  // Calcular o tamanho do iframe baseado na proporção 16:9
  const calculateIframeSize = () => {
    const windowRatio = dimensions.width / dimensions.height;
    const gameRatio = 16 / 9;
    
    if (windowRatio > gameRatio) {
      // Janela mais larga que o jogo - usar altura como referência
      return {
        width: dimensions.height * 16 / 9,
        height: dimensions.height
      };
    } else {
      // Janela mais estreita que o jogo - usar largura como referência
      return {
        width: dimensions.width,
        height: dimensions.width * 9 / 16
      };
    }
  };

  const iframeSize = calculateIframeSize();

  return (
    <div className="h-screen flex flex-col bg-gray-900 overflow-hidden">
      <main className="flex-1 flex items-center justify-center p-0 overflow-hidden">
        <div 
          className="relative flex items-center justify-center" 
          style={{ 
            width: iframeSize.width, 
            height: iframeSize.height,
            maxWidth: '100vw',
            maxHeight: '100vh'
          }}
        >
          <iframe
            ref={iframeRef}
            src="/godot/index.html"
            title="Jogo ETS"
            className="absolute top-0 left-0"
            style={{ 
              width: '100%', 
              height: '100%', 
              border: 'none', 
              backgroundColor: 'white' 
            }}
          />
        </div>
      </main>
    </div>
  );
}