import {Request, Response, Router} from "express"

// User type
type TUser = {
    name: string
    email: string
}

const router: Router = Router()
let users: TUser[] = []

// Requirement 1
router.get("/hello", (req: Request, res: Response) => {
    res.json({msg: "Hello world!" })
})

// Requirement 2
router.get("/echo/:id", (req: Request, res: Response) => {
    //const { id } = req.params
    res.json({ id: req.params.id })
})

// Requirement 3
router.post("/sum", (req: Request, res: Response) => {
    let result: number = 0
    for (let i = 0; i < req.body.numbers.length; i++) {
        result += req.body.numbers[i]
    }
    res.json({ sum: result })
})

// Requirement 4
router.post("/users", (req: Request, res: Response) => {
    const { name, email } = req.body
    const newUser: TUser = { name, email }
    users.push(newUser)
    // console.log("Current users array:", users)
    res.json({ message: "User successfully added" })
})

// Requirement 5
router.get("/users", (req: Request, res: Response) => {
    res.status(201).json({ users })
})

export default router
