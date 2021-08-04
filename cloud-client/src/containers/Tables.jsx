import React, {useEffect, useState} from 'react';

/**
 *@author Arturo Negreiros
 * this sections will contain the values extracted from the database, that is, cassandra sql
 */


const Tables = () => {
    const [numbers, Setnumbers] = useState([]);
    const APIFlsk = "http://192.168.100.8:5000/test";
    useEffect(() =>{
        fetch(APIFlsk)
            .then(response => response.json())
            .then(data => Setnumbers(data))
    }, []);
    console.log(numbers)
    return (
        <div></div>
    );
}

export default Tables;