type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    let timeOut: any = null
    return function(...args) {
        if (timeOut) {
            clearTimeout(timeOut)
        }
        timeOut = setTimeout(() => {
            fn(...args)
        }, t)
    }
};

let log = debounce((...args) => console.log(...args), 100)
log(1)
log(2)
log(3)