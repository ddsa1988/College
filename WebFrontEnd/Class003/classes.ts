class Person {
    private _fullName: string;
    private _birthdate: Date;

    constructor(fullName: string, birthdate: Date) {
        this.setFullName(fullName);
        this.setBirthdate(birthdate);
    }

    public getFullName(): string {
        return this._fullName;
    }

    public setFullName(value: string): void {
        if (value.trim().length === 0) {
            throw new Error("Name must not be empty.");
        }

        this._fullName = value;
    }

    public getBirthdate(): Date {
        return this._birthdate;
    }

    public setBirthdate(value: Date): void {
        const now: Date = new Date();
        const age = now.getFullYear() - value.getFullYear();

        if (age < 0) {
            throw new Error("Birthdate must be greater than today.");
        }

        this._birthdate = value;
    }

    public toString(): string {
        return `Person [ Full name = ${
            this._fullName
        }, Birthdate = ${this._birthdate.toLocaleDateString()} ]`;
    }
}

class Student extends Person {
    private _id: number;

    constructor(fullName: string, birthdate: Date, id: number) {
        super(fullName, birthdate);
        this.setId(id);
    }

    public getId(): number {
        return this._id;
    }

    public setId(value: number) {
        if (value <= 0) {
            throw new Error("Invalid id");
        }

        this._id = value;
    }

    public override toString(): string {
        return `Person [ Full name = ${this.getFullName()}, Birthdate = ${this.getBirthdate().toLocaleDateString()}, Id = ${
            this._id
        } ]`;
    }
}

let p1: Person = new Person("Diego", new Date("1988-01-22"));
let s1: Student = new Student("Amanda", new Date("1993-10-16"), 1);

console.log(p1.toString());
console.log(s1.toString());
