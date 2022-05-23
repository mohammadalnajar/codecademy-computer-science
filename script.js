// console.log("first");

// const getUserName = (name, callback) => {
//     console.log(1);
//     console.log(name);
//     setTimeout(() => {
//         console.log(2);
//         console.log(name, 342);
//         callback(name, "45egfsd",);
//     }, 2000);
//     console.log(3);
// };

// const getPassword = (name, password, callback) => {
//     console.log(`Hello ${name}`);
//     console.log(4);
//     console.log(password);
//     setTimeout(() => {
//         console.log(5);
//         console.log(password, 342);
//         callback(password);
//     }, 2000);
//     console.log(6);
// };

// getUserName("John", (name) => {}));

// ======================================

const getUserName = (name) => {
    return new Promise((resolve, reject) => {
        if (name) {
            const obj = {
                name: name,
                age: 23,
                study: "IT"
            };
            setTimeout(() => {
                resolve(obj);
            }, 2000);
        } else {
            reject("No name");
        }
    });
};

getUserName("John")
    .then((name) => {
        console.log(name, "then");
    })
    .catch((error) => {
        console.log(error, "catch");
    });

// const logName = async (name) => {
//     try {
//         const user = await fetch("https://randomuser.me/api/");
//         console.log(user, "async");
//     } catch (error) {
//         console.log(error);
//     }
// };

// logName("John");

// promises.all();

// const getName = (wefdsaga) => {
//     const name = wefdsaga ? "john" : "no name";
//     return name;
// };

// console.log(getName());
