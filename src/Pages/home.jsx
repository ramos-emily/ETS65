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
    function handleResize() {
      setDimensions({
        width: window.innerWidth,
        height: window.innerHeight
      });
    }

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const handleFullscreen = () => {
    const iframe = iframeRef.current;
    if (iframe && iframe.requestFullscreen) {
      iframe.requestFullscreen();
    } else if (iframe && iframe.webkitRequestFullscreen) { // Safari
      iframe.webkitRequestFullscreen();
    } else if (iframe && iframe.msRequestFullscreen) { // IE11
      iframe.msRequestFullscreen();
    }
  };

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
    <div className="h-screen flex flex-col bg-black overflow-hidden">
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
          
          {/* Botão de tela cheia */}
          <button 
            onClick={handleFullscreen}
            className="absolute bottom-2 right-2 bg-blue-600 hover:bg-blue-700 text-white p-2 rounded-md opacity-80 hover:opacity-100 transition-all z-10"
            title="Tela Cheia"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5v-4m0 4h-4m4 0l-5-5" />
            </svg>
          </button>
        </div>
      </main>
    </div>
  );
}