import React from 'react';


const TestValues = () => {
    return (
        <div className="container p-4">
            <form id="FormSignup" action="/aut/signup" method="POST" encType="multipart/form-data">
                <div>
                    <div className="form-group col-md-6">
                        <label htmlFor="inputCed">Cedula o identificador</label>
                        <input required type="text" className="form-control" id="inputCed"
                            name="credencials" />
                        <label htmlFor="inputCed">Cedula o identificador</label>
                        <input required type="text" className="form-control" id="inputCed"
                            name="credencials" />
                    </div>
                    <div className="form-group col-md-6">
                        <label htmlFor="inputCed">Cedula o identificador</label>
                        <input required type="text" className="form-control" id="inputCed"
                            name="credencials" />
                    </div>
                    <div className="form-row">
                        <div className="form-group col-md-6">
                            <label htmlFor="inputNombre">Nombres</label>
                            <input required type="text" className="form-control" id="inputNombre" name="name" autoFocus />
                        </div>
                        <div className="form-group col-md-6">
                            <label htmlFor="inputApellido">Apellidos</label>
                            <input required type="text" className="form-control" id="inputApellido" name="lname" />
                        </div>
                        <div className="form-group col-md-6">
                            <label htmlFor="inputEmail">Email</label>
                            <input required type="email" className="form-control" id="inputEmail" name="email" name="email" />
                        </div>
                    </div>
                    <div className="form-row">

                        <div className="form-group col-md-12">
                            <label htmlFor="inputOcupation">Ocupación</label>
                            <select id="inputOcupation" className="form-control" name="ocupation">
                                <option defaultValue>Estudiante de ingeniería</option>
                                <option>Profesional de desarrollo</option>
                            </select>
                        </div>
                        <div className="form-group col-md-4">
                            <label htmlFor="inputUser">Usuario</label>
                            <input required type="text" className="form-control" id="inputUser" name="user" />
                        </div>
                        <div className="form-group col-md-4">
                            <label htmlFor="inputPass">Contraseña</label>
                            <input required type="password" className="form-control" id="inputPass" name="password" />
                        </div>
                        <div className="form-group col-md-4">
                            <label htmlFor="inputPass2">Vuelva a ingresar la contraseña</label>
                            <input required type="password" className="form-control" id="inputPass2" name="password2" />
                        </div>
                    </div>


                </div>
                <button type="submit" id="BtnSubmitForm" className="btn btn-success">Registrar</button>
            </form>


        </div>
    );
};

export default TestValues;