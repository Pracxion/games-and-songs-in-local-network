import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import httpClient from '../../httpClient';
import { User } from '../../types/user';

const HubPage: React.FC = () => {
    const navigate = useNavigate();
    const [user, setUser] = useState<User | null>(null);

    useEffect(() => {
        (async () => {
            try {
                const resp = await httpClient.get("/@me");
                setUser(resp.data);
            } catch (error) {
                console.log("Not authenticated");
            }
        })();
    }, []);

    return <div>

    </div>
}

export default HubPage;