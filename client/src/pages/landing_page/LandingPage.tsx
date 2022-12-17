import React, { useCallback, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { BiArrowBack } from "react-icons/bi";
import httpClient from '../../httpClient';
import { User } from '../../types/user';
import './LandingPage.scss';

export const LandingPage: React.FC = () => {
    const navigate = useNavigate();
    const [isLoginScreen, setIsLoginScreen] = useState(true)
    const [username, setUsername] = useState<string>("");
    const [forname, setForname] = useState<string>("");
    const [surname, setSurname] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const setIsLoginScreenTrue = useCallback((): void => setIsLoginScreen(true), []);
    const setIsLoginScreenFalse = useCallback((): void => setIsLoginScreen(false), []);

    useEffect(() => {
        setUsername('');
        setForname('');
        setSurname('');
        setPassword('');
    }, [])

    const logInUser = async () => {
        try {
            const response = await httpClient.post(
                "/login",
                JSON.stringify({
                    username,
                    password,
                }), {
                headers: { 'Content-Type': 'application/json' },
                withCredentials: true
            });
            setUsername('');
            setPassword('');
            // TODO Handle Success
            navigate('/@me')
        } catch (error: any) {
            if (error.response.status === 401) {
                alert("Invalid credentials");
            }
        }
    };

    const registerUser = async () => {
        try {
            const response = await httpClient.post(
                "/register",
                JSON.stringify({
                    username,
                    forname,
                    surname,
                    password
                }), {
                headers: { 'Content-Type': 'application/json' },
                withCredentials: true
            });
            setUsername('');
            setForname('');
            setSurname('');
            setPassword('');
            // TODO Handle Success
            navigate('/@me')
        } catch (error: any) {
            console.log(error)
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
                            value={forname}
                            onChange={(e) => setForname(e.target.value)}
                            id="registerForename"
                        />
                    </div>
                    <div className='input-group'>
                        <label>Nachname</label>
                        <input
                            type="text"
                            value={surname}
                            onChange={(e) => setSurname(e.target.value)}
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
                    <button type="button" onClick={() => registerUser()}>
                        Registrieren
                    </button>
                </form>
            </div>
        }
    </div>;
}
