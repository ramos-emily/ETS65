import React from "react";
import colorbar from "/linha-colorida.png";
import boschLogo from "/Bosch-logo.png";

export default function HeaderBosch() {
  return (
    <header className="w-full">
      <div className="w-full overflow-hidden">
        <img
          src={colorbar}
          alt="Barra colorida decorativa"
          className="w-full h-1 sm:h-2 md:h-3 object-cover block"
        />
      </div>

      <div className="w-full bg-white shadow-md">
        <div
          className="
            mx-auto flex items-center justify-between
            w-full max-w-screen-3xl
            px-4 sm:px-6 md:px-8
            h-14 sm:h-16 md:h-[70px]
          "
        >
          <h1
            className="
              text-md sm:text-xl md:text-2xl
              font-bold text-black
              leading-none
            "
          >
            Desafio ETS
          </h1>

          <div className="h-full flex items-center">
            <img
              src={boschLogo}
              alt="Bosch"
              className="
                h-10 sm:h-12 md:h-[70px]
                w-auto object-contain select-none
              "
              draggable={false}
            />
          </div>
        </div>

        <div className="md:h-[10px]" />
      </div>
    </header>
  );
}
