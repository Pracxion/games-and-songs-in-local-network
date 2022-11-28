import React, { useState } from 'react';
import { BiArrowBack } from "react-icons/bi";

export const RegisterForm = (props: { toggle: CallableFunction}) => {

    const [username, setUsername] = useState<string>("");
    const [forename, setForename] = useState<string>("");
    const [surename, setSurename] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    return <div>
        <button onClick={props.toggle()}><BiArrowBack /></button>
        <form>
            <div>
                <label>Username: </label>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    id="registerUsername"
                />
            </div>
            <div>
                <label>Vorname: </label>
                <input
                    type="text"
                    value={forename}
                    onChange={(e) => setForename(e.target.value)}
                    id="registerForename"
                />
            </div>
            <div>
                <label>Nachname: </label>
                <input
                    type="text"
                    value={surename}
                    onChange={(e) => setSurename(e.target.value)}
                    id="registerSurename"
                />
            </div>
            <div>
                <label>Passwort: </label>
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
    </div>;
}