import MonkeyHeadSvg from '@/assets/svg-components/MonkeyHead.svg';
import MonkeNameSvg from '@/assets/svg-components/MonkeyName.svg';
import Stack from '@mui/material/Stack';

import classes from './MonkeyLogo.module.scss';
import { useTheme } from '@mui/material/styles';

const MonkeyLogo = (props) => {
    const theme = useTheme();

    return (
        <Stack
            className={classes.monkeyLogo}
            direction="row"
            useFlexGap
            style={{
                zIndex: 100,
                background: 'black',
                boxShadow: '0 0 20px 20px black',
                marginBottom: '-30px'
            }}
            {...props}>
            <MonkeyHeadSvg
                className={classes.logo}
                color={theme.palette.primary.main}
            />
            <MonkeNameSvg
                className={classes.name}
                color={theme.palette.primary.main}
            />
        </Stack>
    );
};

export default MonkeyLogo;
