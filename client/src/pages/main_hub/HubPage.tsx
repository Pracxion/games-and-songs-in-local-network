import React, { useEffect, useState } from 'react';
import httpClient from '../../httpClient';
import { User } from '../../types/user';

const HubPage: React.FC = () => {

    const [user, setUser] = useState<User | null>(null);

    useEffect(() => {
        (async () => {
            try {
                const resp = await httpClient.get("/@me");
                console.log(resp)
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