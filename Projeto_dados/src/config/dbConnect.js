import mongoose from "mongoose";


async function connectDataBase(){
    mongoose.connect("mongodb+srv://lucasluc1207:87500273@cluster0.li8djjr.mongodb.net/adotaeu?retryWrites=true&w=majority");
    
    return mongoose.connection;
}

export default connectDataBase;

