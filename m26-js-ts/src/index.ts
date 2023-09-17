
import util from "util";

let func = process.argv[2];

switch (func) {
    case "xxx":
        xxx();
        break;
    case "yyy":
        yyy();
        break;
    default:
        displayCommandLineExamples();
        break;
}

function xxx() {
    console.log(util.format('  xxx; count: %s', 1));
}

function yyy() {
    console.log(util.format('  yyy; count: %s', 1));
}
function displayCommandLineExamples() {
    console.log('');
    console.log("node .\\dist\\index.js hello Luciano");
    console.log("node .\\dist\\index.js xxx");
    console.log("node .\\dist\\index.js yyy <aaa> <bbb> <ccc>");
    console.log('');
}
