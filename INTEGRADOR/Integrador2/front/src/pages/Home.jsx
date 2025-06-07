import React, { useState } from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
  Filler
} from "chart.js";
import axios from "axios";

ChartJS.register(
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
  Filler
);

export const Home = () => {
  const [dados, setDados] = useState([]);
  const [sensorIdInput, setSensorIdInput] = useState("");
  const [sensorIdFiltro, setSensorIdFiltro] = useState("");
  const [loading, setLoading] = useState(false);
  const url = "historico";

  const fetchDados = () => {
    if (!sensorIdInput) return;
    setLoading(true);
    const token = localStorage.getItem("token");

    const filtro = `?sensor=${sensorIdInput}`;

    axios
      .get(`http://127.0.0.1:8000/${url}/search/${filtro}`, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => {
        setDados(res.data);
        setSensorIdFiltro(sensorIdInput);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Erro ao buscar dados:", err);
        setDados([]);
        setLoading(false);
      });
  };

  const labels = dados.map((item) => item.timestamp || "");
  const valores = dados.map((item) => Number(item.valor || 0));

  const data = {
    labels,
    datasets: [
      {
        label: `Valor por Timestamp (Sensor ${sensorIdFiltro})`,
        data: valores,
        borderColor: "rgb(75, 192, 192)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        tension: 0.3,
        fill: true,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      title: { display: true, text: "Gráfico de Leitura de Sensores" },
      legend: { position: "top" },
    },
  };

  return (
    <div className="min-h-screen flex flex-col justify-center items-center p-4 gap-6">
      <h2 className="text-xl font-semibold mb-4 text-center">Dashboard</h2>

      <div className="flex gap-2">
        <input
          type="text"
          placeholder="Digite o ID do sensor"
          value={sensorIdInput}
          onChange={(e) => setSensorIdInput(e.target.value)}
          className="border border-gray-300 rounded px-3 py-1"
        />
        <button
          onClick={fetchDados}
          className="bg-blue-600 text-white px-4 py-1 rounded hover:bg-blue-700"
          disabled={loading}
        >
          {loading ? "Carregando..." : "Filtrar"}
        </button>
      </div>

      <div className="w-[500px]">
        <Line data={data} options={options} />
      </div>
    </div>
  );
};
