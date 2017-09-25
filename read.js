var fs = require('fs');
var parse = require('csv-parse');

var Data=[];
fs.createReadStream('uploads/Ad_Credit-.csv')
	.pipe(parse())
	.on('data' , function(csvrow){
	console.log(csvrow);
	Data.push(csvrow);
})
.on('end',function() {
    console.log("jjj");
});
