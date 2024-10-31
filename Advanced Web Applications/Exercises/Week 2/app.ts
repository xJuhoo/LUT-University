// Requirement 1
console.log("Hello World!");

// Requirement 2
type TVehicle = {
    model: string,
    color: string,
    year: number,
    power: number,
};

const vehicle: TVehicle = {
    model: "Boring generic vehicle",
    color: "Red",
    year: 1993,
    power: 60,
};

console.log(vehicle);

// Requirement 3
interface IVehicle {
    model: string,
    color: string,
    year: number,
    power: number,
};

interface ICar extends IVehicle {
    bodyType: string,
    wheelCount: number,
};

interface IBoat extends IVehicle {
    draft: number,
};

interface IPlane extends IVehicle {
    wingspan: number,
};

const car: ICar = {
    model: "Ford focus",
    color: "Green",
    year: 2016,
    power: 150,
    bodyType: "Hatchback",
    wheelCount: 4,
};

const plane: IPlane = {
    model: "Boeing 777",
    color: "White",
    year: 2020,
    power: 170000,
    wingspan: 65,
};

const boat: IBoat = {
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
class VehicleService<T> {
    private items: T[] = [];

    // Learned to create functions inside class from:
    // https://stackoverflow.com/questions/49582627/define-typescript-class-method
    add(vehicle: T): void {
        this.items.push(vehicle);
    }

    list(): T[] {
        return this.items;
    }
}

const cars = new VehicleService<ICar>();
cars.add(car);

const boats = new VehicleService<IBoat>();
boats.add(boat);

console.log(cars.list());
console.log(boats.list());
