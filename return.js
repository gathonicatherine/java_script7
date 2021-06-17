// class StoreCalc{
//     constructors(shoes,price){
//         this.shoes = "Vans";
//         this.price = 1200;
//         this.quality = 1;

//         this.shoes = "Airforce";
//         this.price = 2500;
//         this.quality = 1;

//         this.shoes = "Slides";
//         this.price = 600;
//         this.quality = 1;


//     }
// getTotalCost(){
//     return "${this.quality}${this.shoes} for KES ${this.price*this.quality}";

// }
// getTotalCost(){
//     return "${this.quality}${this.shoes} for KES ${this.price*this.quality1}";
// }
// getTotalCost(){
//     return "${this.quality}${this.shoes} for KES ${this.price*this.quality2}";
// }
// }
// var shoes = new shoes("Vans", 1);
// console.log(shoes.getTotalCost());

// var shoes = new shoes("Airforce, 1");
// console.log(shoes.getTotalCost1());

// var shoes = new shoes("Slides", 1);
// console.log(shoes.getTotalCost2());
// function prepare(ingredients,callback){
//     console.log(`preparing ${ingredients}`)
//     callback();
// }
// function chop(){
//     console.log("chopping");
//     };
//     prepare("Tomatoes and Onions", chop);

//     function cook(methods,callback){
//         console.log(`cooking ${methods}`)
//         callback();
//     }
//     function pika(){
//         console.log("cooking");
//     };
//     cook("Ugali is so easy, all you have to do is boil water then add floor and stir.......walaaaaah! your ugali is ready",pika);

// const posts=[
//     {
//         title :`Born A Crime`,
//         author:`Trevor Noah`
//     },
//     {
//     title:`Think Big`,
//     author:`Ben Conson`
//     }
// ]
// function getPosts(){
//     setTimeout(()=>{
//         let output='';
//         posts.forEach((post)=>{
//             output +=`${post.title}`
//         });
//         console.log(output);
//     },1000);
// }
//     function createPosts(post,callback){
//         setTimeout(()=>{
//             posts.push(post);
//             callback();
//         },2000);
//     }
//     getPosts();
//     createPosts({title: "To kill a Mockingbird", 
//     author : "Haper Lee"},
//     getPosts);
// function leapYear(years){
//     if(years%4==0){
//         return(`${years} is a leap year`)
//     }else{
//         return(`${years} is not a leap year`)
//     }
// }
// console.log(leapYear(2020))
// console.log(leapYear(2017))

// function leapyears(years){
//     if(years%4==0){
//         return(`${years} is not leap year`)
//     }else{
//         return(`${years} is a leap year`)
//     }
// }
// console.log(leapyears(2021))
// console.log(leapyears(2121))
//



// ARRAYS
// let fruits = [`fruits`,`Apple`]
// console.log(fruits.length)

// let first=fruits [0]
// console.log(first)

// let last=fruits[1]
// console.log(last) 









var library = [
    {
        title: 'Bill Gates',
        author: 'The Road Ahead',
        readingStatus: true
    },
    {
        title: 'Steve Jobs',
        author: 'Walter Isaacson',
        readingStatus: true
    },
    {
        title: 'Mockingjay: The Final Book of The Hunger Games',
        author: 'Suzanne Collins',
        readingStatus: false
    }];
for (var i = 0; i < library.length; i++)
   {
    var book = "'" + library[i].title + "'" + ' by ' + library[i].author + ".";
    if (library[i].readingStatus) {
      console.log("Already read " + book);
    } else
    {
     console.log("You still need to read " + book);
    }
   }
