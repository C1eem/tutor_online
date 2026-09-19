export {}

const delay = (ms: number): Promise<void> =>
    new Promise<void>(resolve => setTimeout(resolve, ms))

const fail = (ms: number): Promise<never> => 
    new Promise<never>((_, reject) => 
        setTimeout(() => reject(new Error("Boom")), ms)
    )

type User = {
    id: number
    name: string
}

type Course = {
    title: string
    price: number
}

// Функция fakeFetchUsers(): Promise<User[]> — имитирует запрос к бэку.
// Через delay(500) возвращает массив:
//   [{ id: 1, name: "Иван" }, { id: 2, name: "Мария" }]
// Подсказка:
//   async function fakeFetchUsers(): Promise<User[]> {
//     await delay(500)
//     return [...]
//   }

async function fakeFetchUsers(): Promise<User[]> {
    await delay(500)
    return [{ id: 1, name: "Иван" }, { id: 2, name: "Мария" }]
}

// 1. Вызови через async/await и выведи результат.

// 2. Оберни в try/catch на случай ошибки (на будущее)


// Функция fakeFetchCourses(success: boolean): Promise<Course[]>
// Если success — возвращает массив курсов через delay(300).
// Если не success — через delay(300) бросает new Error("Network error")\
async function fakeFetchCourses(success: boolean): Promise<Course[]> {
    await delay(300)
    if (!success) {
        throw new Error("Network error")
    }
    return [{title: "A", price: 100}, {title: "B", price: 200}]
} 

// 1. Вызови с success=true — выведи данные.
// 2. Вызови с success=false — поймай ошибку, выведи e.message.
// 3. Оберни вызов в try/catch/finally, в finally выведи "загрузка завершена".



// Запусти параллельно три fakeFetchUsers() с разными задержками:
//   const [a, b, c] = await Promise.all([
//     fakeFetchUsers(),
//     fakeFetchUsers(),
//     fakeFetchUsers(),
//   ])
// Замерь время через Date.now() до и после — убедись,
// что все три выполнились за ~500ms, а не за 1500ms.


async function elapsed_time() {
    const time = Date.now()
    const [a, b, c] = await Promise.all([
        fakeFetchUsers(),
        fakeFetchUsers(),
        fakeFetchUsers(),
    ])
    console.log(`Time: ${Date.now() - time}`)
}

// elapsed_time()

// type State = {
//   data: User[] | null
//   loading: boolean
//   error: string | null
// }

// Функция loadUsers(): Promise<State> — имитирует полный цикл:
// 1. Начальное состояние: { data: null, loading: true, error: null }
// 2. Вызвать fakeFetchUsers()
// 3. Если успех — вернуть { data, loading: false, error: null }
// 4. Если ошибка — вернуть { data: null, loading: false, error: e.message }

// Выведи через console.log результат на каждом этапе.

type State = {
    data: User[] | null
    loading: boolean
    error: string | null
}

async function loadUsers(): Promise<State> {
    try {
        const users = await fakeFetchUsers()
        return {data: users, loading: false, error: null}
    } catch (e) {
        const errorMessage = e instanceof Error ? e.message : "Unknown Error"
        return {data: null, loading: false, error: errorMessage}
    }
}