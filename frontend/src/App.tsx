// import { useEffect, useState } from "react";

// function App() {
//   const [message, setMessage] = useState<string | null>(null)
//   const [loading, setLoading] = useState(true)
//   const [error, setError] = useState<string | null>(null)

//   useEffect(() => {
//     const load = async () => {
//       try {
//         const res = await fetch("http://localhost:8000/")
//         if (!res.ok) throw new Error(`HTTP ${res.status}`)
//         const data = await res.text()
//         setMessage(data)
//       } catch (e) {
//         setError(e instanceof Error ? e.message : "Unknown error")
//       } finally {
//         setLoading(false)
//       }
//     }
//     load()
//   }, [])

//   if (loading) return <p>Загрузка...</p>
//   if (error) return <p style={{ color: "red" }}>Ошибка: {error}</p>

//   return (
//     <div>
//       <h1>Ответ от бэка:</h1>
//       <p>{message}</p>
//     </div>
//   )
// }

// export default App

import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const load = async () => {
      try {
        const res = await fetch("http://localhost:8000/")
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        const data = await res.text()
        setMessage(data)
      } catch (e) {
        setError(e instanceof Error ? e.message : "Unknown error")
      } finally {
        setLoading(false)
      }
    }

    load()

  }, [])

  if (loading) return <p>Загрузка...</p>
  if (error) return <p style={{ color: "red" }}>Ошибка: {error}</p>

  return (
    <div>
      <h1>Ответ с бэка:</h1>
      <p>{message}</p>
    </div>
  )
}

export default App