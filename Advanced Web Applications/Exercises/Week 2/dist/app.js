"use strict";
// Requirement 1
console.log("Hello World!");
const vehicle = {
    model: "Boring generic vehicle",
    color: "Red",
    year: 1993,
    power: 60,
};
console.log(vehicle);
;
;
;
;
const car = {
    model: "Ford focus",
    color: "Green",
    year: 2016,
    power: 150,
    bodyType: "Hatchback",
    wheelCount: 4,
};
const plane = {
    model: "Boeing 777",
    color: "White",
    year: 2020,
    power: 170000,
    wingspan: 65,
};
const boat = {
    model: "Bella",
    color: "Black",
    year: 2022,
    power: 100,
    draft: 0.42,
};
console.log(car);
console.log(plane);
console.log(boat);
// Requirement 4
class VehicleService {
    items = [];
    add(vehicle) {
        this.items.push(vehicle);
    }
    list() {
        return this.items;
    }
}
const cars = new VehicleService();
cars.add(car);
const boats = new VehicleService();
boats.add(boat);
console.log(cars.list());
console.log(boats.list());
