interface IPerson {
    firstName: string;
    birthdate: Date;
    active: boolean;
}

let person: IPerson = {
    firstName: "Diego",
    birthdate: new Date("1988-01-22"),
    active: true,
};
