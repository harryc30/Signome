//let button;
function mouseClicked() {
    fetch('/postmethod')
    .then(function (response) {
        return response.text();
    }).then(function (hitext) {
        console.log('GET response text:');
        console.log(hitext); // Print the greeting as text
        fill(5);
        textSize(38)
        textFont("Average")
        text(hitext, 800, 200, 100, 100);
    });
} 
function setup() {
    createCanvas(1280, 1200);
    //button = createButton('Transcribe Image');
    //button.position(790,185);
    //button.mousePressed(mouseClicked);
}
function draw() {
    strokeWeight(0);
    fill(235,236,240);
    rect(300,55,404,50,20);

    //strokeWeight(0);
    //fill(235,236,240);
    //rect(775,167,404,420,20);
}
