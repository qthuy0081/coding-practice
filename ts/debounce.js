function debounce(fn, t) {
    var timeOut = null;
    return function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        if (timeOut) {
            clearTimeout(timeOut);
        }
        timeOut = setTimeout(function () {
            fn.apply(void 0, args);
        }, t);
    };
}
;
var log = debounce(function () {
    var args = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        args[_i] = arguments[_i];
    }
    return console.log.apply(console, args);
}, 100);
log(1);
log(2);
log(3);
