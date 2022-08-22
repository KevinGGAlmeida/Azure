import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import Api from './api'


export default() =>{
    const [user,setUser] = useState();

    useEffect(() => {
        Api.get("/?format=json").then((response) => setUser(response.data)).catch((err) =>{
            console.log(err.response.data);
            console.log(err.response.status);
            console.log(err.response.headers)})
    });
    console.log(user['id'])
    return(
            <div>
                <h2>{user?.Descricao}
                </h2>
                foi?
            </div>
    )
}
