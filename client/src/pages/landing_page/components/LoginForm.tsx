import React, { useState } from 'react';
import httpClient from '../../../httpClient';

export const LoginForm = () => {

    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const logInUser = async () => {
        console.log(username, password);
        try {
            const resp = await httpClient.post("/login", {
                username,
                password,
            });

            window.location.href = "/";
        } catch (error: any) {
            if (error.response.status === 401) {
                alert("Invalid credentials");
            }
        }
    };

    const goToRegister = () => {
        window.location.href = "/register";
    };

    return <div>
        <form>
            <div>
                <label>Username: </label>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    id='loginUsername'
                />
            </div>
            <div>
                <label>Passwort: </label>
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    id='loginPassword'
                />
            </div>
            <button type="button" onClick={() => logInUser()}>
                Anmelden
            </button>
        </form>
        <p>oder hier <button onClick={() => goToRegister()}>Anmelden</button></p>
    </div>;
}