import React, { useState } from "react";
import { MapaSensor } from "../components/MapaSensor";
import { ModalFilter } from "../components/modalFilter";
import filter from "../assets/filter.svg";

export function Home() {
  const [modalFilter, setModalFilter] = useState(false);
  const [sensorSelecionado, setSensorSelecionado] = useState(null);

  return (
    <main className="flex flex-col items-center justify-center min-h-screen pt-32 pb-16 gap-6 px-4">
      <h1 className="text-2xl font-bold text-[#226D13]">Localização do Sensor</h1>

      <button
        onClick={() => setModalFilter(true)}
        className="bg-white shadow-md rounded p-2 hover:shadow-lg transition-all cursor-pointer"
      >
        <img src={filter} alt="Filtrar sensor" className="w-6 h-6" />
      </button>

      {sensorSelecionado ? (
        <div className="w-full max-w-[700px]">
          <MapaSensor
            latitude={sensorSelecionado.latitude}
            longitude={sensorSelecionado.longitude}
            nome={sensorSelecionado.sensor}
          />
        </div>
      ) : (
        <p className="text-[#226D13] font-medium">Nenhum sensor selecionado</p>
      )}

      <ModalFilter
        isOpen={modalFilter}
        onClose={() => setModalFilter(false)}
        url="sensores"
        campos={["id", "sensor", "mac_address", "unidade_medida", "latitude", "longitude", "status"]}
        onSensorSelect={(sensor) => {
          setSensorSelecionado(sensor);
          setModalFilter(false);
        }}
      />
    </main>
  );
}
