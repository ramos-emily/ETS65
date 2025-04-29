import styles from "./Login.module.css";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useNavigate } from "react-router-dom"; 

const loginSchema = z.object({
  email: z.string()
    .email({message: 'Informe um e-mail válido!'}) ,
  senha: z.string()
    .length(6, {message: 'Defina uma senha de 6 caracteres!'})
});

export function Login() {
  const navigate = useNavigate(); 

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(loginSchema),
  });

  function userAutenticate(data) {
    navigate("/inicial"); 
  }

  return (
    <div className={styles.container}>
      <p className={styles.title}>LOGIN</p>

      <form onSubmit={handleSubmit(userAutenticate)} className={styles.form}>
        <input {...register("email")} placeholder="Email" className={styles.field} />
        {errors.ni && <p>{errors.ni.message}</p>}
        <input {...register("senha")} placeholder="Senha" className={styles.field} />
        {errors.ni && <p>{errors.ni.message}</p>}

        <button type="submit" className={styles.button}>
          Logar
        </button>
      </form>
    </div>
  );
}
