import { useRef } from "react";
import HeaderBosch from "../Components/Header/header";
import time from "/time.png";
import Footer from "../Components/Footer/footer";

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

  return (
    <>
      <HeaderBosch />

      <div className="relative z-10 mx-auto w-full max-w-screen-xl px-6 sm:px-6 md:px-10 py-12 sm:py-16 md:py-20">
        <h1 className="text-center text-lg sm:text-3xl md:text-4xl font-bold text-black px-2 mb-0 sm:mb-6 md:mb-24 lg:mb-24">
          65 anos da ETS - Desafio do Conhecimento
        </h1>

        <div className="mt-6 sm:mt-8 md:mt-0 flex flex-col md:flex-row items-center justify-between gap-6 sm:gap-8 md:gap-12">
          <div className="flex-1 text-black text-justify max-w-3xl">
            <h2 className="text-md sm:text-2xl md:text-3xl font-semibold mb-3 sm:mb-4 md:mb-6">
              Quiz 65 anos ETS
            </h2>
            <p className="text-xs sm:text-lg md:text-xl leading-relaxed">
              Bem-vindo(a) ao nosso jogo especial em comemoração aos 65 anos da ETS!
              São mais de seis décadas de história, aprendizado e inovação. Ao longo desse tempo,
              milhares de alunos, instrutores e colaboradores ajudaram a construir a nossa trajetória,
              transformando vidas e deixando um legado que continua crescendo.
            </p>
          </div>

          <div className="flex justify-end items-center">
            <img
              src={time}
              alt="Time ETS"
              className="object-contain h-56 sm:h-72 md:h-[26rem] w-auto"
            />
          </div>
        </div>
      </div>

      <section className="w-full">
        <div className="mx-auto w-full max-w-screen-xl px-4 sm:px-6 md:px-10 mt-6 sm:mt-8 md:mt-10">
          <h2 className="text-md sm:text-3xl md:text-4xl font-semibold text-black">
            Vamos testar o quanto você sabe?
          </h2>
        </div>

        <div className="mx-auto w-full max-w-screen-xl px-4 sm:px-6 md:px-10 mt-3 sm:mt-4 flex justify-end">
          <button
            onClick={handleFullscreen}
            className="
              bg-[#007BC0] text-white py-2 px-2 sm:px-6
              text-[8px] sm:text-base hover:bg-[#00629A] transition-colors
            "
          >
            TELA CHEIA
          </button>
        </div>

<div className="mx-auto w-full max-w-[80vw] px-2 sm:px-4 md:px-4 mt-6 sm:mt-8 md:mt-10 mb-8 sm:mb-10 md:mb-[50px]">
  <div className="w-full aspect-[16/9]">
    <iframe
      ref={iframeRef}
      src="/godot/index.html"
      title="Jogo ETS"
      className="w-full h-full"
      style={{ border: "none", backgroundColor: "white" }}
    />
  </div>
</div>
      </section>

      <Footer />
    </>
  );
}
