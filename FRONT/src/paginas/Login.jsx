import styles from "./Login.module.css";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useNavigate } from "react-router-dom"; 

const loginSchema = z.object({
  ni: z.string().length(7, { message: "Insert a valid ni" }),
  name: z.string().min(3, { message: "Insert a valid name" }),
  email: z.string().email({ message: "Insert a valid email" }),
  cellphone: z.string().min(10, { message: "Insert a valid cellphone" }),
  birthDate: z.string().transform((value) => new Date(value)),
  hiringDate: z.string().transform((value) => new Date(value)),
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
        <input {...register("ni")} placeholder="NI" className={styles.field} />
        {errors.ni && <p>{errors.ni.message}</p>}

        <input
          {...register("name")}
          placeholder="Nome"
          className={styles.field}
        />
        {errors.name && <p>{errors.name.message}</p>}

        <input
          {...register("email")}
          placeholder="Email"
          className={styles.field}
        />
        {errors.email && <p>{errors.email.message}</p>}

        <input
          {...register("cellphone")}
          placeholder="Telefone"
          className={styles.field}
        />
        {errors.cellphone && <p>{errors.cellphone.message}</p>}

        <input
          {...register("birthDate")}
          placeholder="Data de nascimento"
          className={styles.field}
          type="date"
        />
        {errors.birthDate && <p>{errors.birthDate.message}</p>}

        <input
          {...register("hiringDate")}
          placeholder="Data de contratação"
          className={styles.field}
          type="date"
        />
        {errors.hiringDate && <p>{errors.hiringDate.message}</p>}

        <button type="submit" className={styles.button}>
          Logar
        </button>
      </form>
    </div>
  );
}
