"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const router = (0, express_1.Router)();
let users = [];
// Requirement 1
router.get("/hello", (req, res) => {
    res.json({ msg: "Hello world!" });
});
// Requirement 2
router.get("/echo/:id", (req, res) => {
    //const { id } = req.params
    res.json({ id: req.params.id });
});
// Requirement 3
router.post("/sum", (req, res) => {
    let result = 0;
    for (let i = 0; i < req.body.numbers.length; i++) {
        result += req.body.numbers[i];
    }
    res.json({ sum: result });
});
// Requirement 4
router.post("/users", (req, res) => {
    const { name, email } = req.body;
    const newUser = { name, email };
    users.push(newUser);
    // console.log("Current users array:", users);
    res.json({ message: "User successfully added" });
});
// Requirement 5
router.get("/users", (req, res) => {
    res.status(201).json({ users });
});
exports.default = router;
