import React from "react";

import {
    Card,
    CardHeader,
    CardBody,
    Flex,
    Box,
    Avatar,
    Heading
} from "@chakra-ui/react";

// TODO: make card span a fixed length

const LandingPage = () => {
    return (
        <Box bg="#171a21" minH="100vh">
        <Flex justify="center" align="center" h="100vh" style={{
            margin: 'auto'
        }}>
            <Card bg='#1b2838'>
            <CardHeader color='azure'>Steam Analysis</CardHeader>
            <CardBody>
                <Flex justifyContent="space-between" alignItems="center">
                <Avatar name="ito" src="../../public/ito_pfp.png" />
                <Heading color="azure" size="md">ito</Heading>
                </Flex>
            </CardBody>
            </Card>
        </Flex>
        </Box>
    );
};

export default LandingPage;