import React, { useCallback, useState } from 'react';
import { BiArrowBack } from "react-icons/bi";
import httpClient from '../../httpClient';
import './LandingPage.scss';

const LandingPage: React.FC = () => {

    const [isLoginScreen, setIsLoginScreen] = useState(true)

    const [username, setUsername] = useState<string>("");
    const [forename, setForename] = useState<string>("");
    const [surename, setSurename] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const setIsLoginScreenTrue = useCallback((): void => setIsLoginScreen(true), []);
    const setIsLoginScreenFalse = useCallback((): void => setIsLoginScreen(false), []);

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

    return <div>
        {isLoginScreen ?
            <div>
                <h1>Login</h1>
                <form className='form-group'>
                    <div className='input-group'>
                        <label >Username</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            id='loginUsername'
                        />
                    </div>
                    <div className='input-group'>
                        <label>Passwort</label>
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
                <p>oder hier <button onClick={setIsLoginScreenFalse}>Anmelden</button></p>
            </div>
            :
            <div>
                <button className='backwards-arrow' onClick={setIsLoginScreenTrue}><BiArrowBack /></button>
                <h1>Registrieren</h1>
                <form className='form-group'>
                    <div className='input-group'>
                        <label>Username</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            id="registerUsername"
                        />
                    </div>
                    <div className='input-group'>
                        <label>Vorname</label>
                        <input
                            type="text"
                            value={forename}
                            onChange={(e) => setForename(e.target.value)}
                            id="registerForename"
                        />
                    </div>
                    <div className='input-group'>
                        <label>Nachname</label>
                        <input
                            type="text"
                            value={surename}
                            onChange={(e) => setSurename(e.target.value)}
                            id="registerSurename"
                        />
                    </div>
                    <div className='input-group'>
                        <label>Passwort</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            id="registerPassword"
                        />
                    </div>
                    <button type="button">
                        Registrieren
                    </button>
                </form>
            </div>
        }
    </div>;
}

export default LandingPage;