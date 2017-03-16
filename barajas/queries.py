def create_data_table_completados():
    return "CREATE TABLE IF NOT EXISTS `piloto_algeciras`.`completados` (" \
           "`FechaInicio` VARCHAR(19)," \
           "`FechaFin` VARCHAR(19)," \
           "`Hash` VARCHAR(44)," \
           "`Instalacion` VARCHAR(11)," \
           "`ModuloIdentificacion` VARCHAR(11)," \
           "`TipoDocumento` VARCHAR(26)," \
           "`PaisEmisor` VARCHAR(3)," \
           "`Sexo` VARCHAR(11)," \
           "`Edad` INT," \
           "`ResultadoFinal` INT," \
           "`ResultVerificacionBiometria` INT," \
           "`ResultVerificacionFacial` INT," \
           "`ResultVerificacionDactilar` INT," \
           "`ResultVerificacionFisica` INT," \
           "`ResultVerificacionChip` INT," \
           "`ResultVerificacionMrz` INT," \
           "`ResultVerificacionDocumental` INT," \
           "`ResultVerificacionARGOSAntecedentes` INT," \
           "`ResultVerificacionARGOSObjetos` INT," \
           "`ResultVerificacionChipPa` INT," \
           "`ResultVerificacionChipAa` INT," \
           "`ResultVerificacionChipCa` INT," \
           "`ResultVerificacionChipTa` INT," \
           "`ResultVerificacionChipBac` INT," \
           "`ResultVerificacionChipRd` INT," \
           "`MensajeErrorVerificacionChip` VARCHAR(255)," \
           "`ScoreReconocimientoFacialVivoChip` REAL," \
           "`ScoreReconocimientoFacialImpresaChip` REAL," \
           "`UmbralAceptacionFacial` INT," \
           "`UmbralRechazoFacial` INT," \
           "`RangoFacial` VARCHAR(5)," \
           "`CalidadFotoCapturada` REAL," \
           "`FiabilidadFotoCapturada` REAL," \
           "`CalidadFotoChip` REAL," \
           "`FiabilidadFotoChip` REAL," \
           "`CalidadFotoImpresa` REAL," \
           "`FiabilidadFotoImpresa` REAL," \
           "`UmbralDactilar` INT," \
           "`RangoDactilar` VARCHAR(3)," \
           "`ScoreMultibiometria` INT," \
           "`UmbralMultibiometria` INT," \
           "`RangoMultibiometria` VARCHAR(3)," \
           "`NombreFuncionBiometrica` VARCHAR(23)," \
           "`TiempoTotalIdentificacion` INT," \
           "`TiempoAccesoSistemaInspeccion` INT," \
           "`TiempoAccesoARGOS` INT," \
           "`TiempoVerificacionDocumento` INT," \
           "`TiempoReconocimientoFacial` INT," \
           "`TiempoReconocimientoDactilar` INT," \
           "`TiempoTotalModuloAcceso` INT," \
           "`TiempoTemplateFacial` INT," \
           "`TiempoTemplateDactilar` INT," \
           "`ScoreDactilar` INT," \
           "`TiempoDesalojarEsclusa` INT," \
           "`TiempoPermanenciaEsclusa` INT," \
           "`TiempoConsultaStatusEES` INT," \
           "`TiempoRegistroEES` INT," \
           "`TiempoObtencionBiometriaEES` INT," \
           "`TiempoVerificacionHuellaEES` INT," \
           "`CalidadH1` INT);"


def generate_query_completados():
    var_string = ', '.join(["%s"] * 60)
    query_string = "INSERT INTO `piloto_algeciras`.`completados` (FechaInicio,FechaFin,Hash,Instalacion,ModuloIdentificacion,TipoDocumento,PaisEmisor,Sexo,Edad,ResultadoFinal,ResultVerificacionBiometria,ResultVerificacionFacial,ResultVerificacionDactilar,ResultVerificacionFisica,ResultVerificacionChip,ResultVerificacionMrz,ResultVerificacionDocumental,ResultVerificacionARGOSAntecedentes,ResultVerificacionARGOSObjetos,ResultVerificacionChipPa,ResultVerificacionChipAa,ResultVerificacionChipCa,ResultVerificacionChipTa,ResultVerificacionChipBac,ResultVerificacionChipRd,MensajeErrorVerificacionChip,ScoreReconocimientoFacialVivoChip,ScoreReconocimientoFacialImpresaChip,UmbralAceptacionFacial,UmbralRechazoFacial,RangoFacial,CalidadFotoCapturada,FiabilidadFotoCapturada,CalidadFotoChip,FiabilidadFotoChip,CalidadFotoImpresa,FiabilidadFotoImpresa,UmbralDactilar,RangoDactilar,ScoreMultibiometria,UmbralMultibiometria,RangoMultibiometria,NombreFuncionBiometrica,TiempoTotalIdentificacion,TiempoAccesoSistemaInspeccion,TiempoAccesoARGOS,TiempoVerificacionDocumento,TiempoReconocimientoFacial,TiempoReconocimientoDactilar,TiempoTotalModuloAcceso,TiempoTemplateFacial,TiempoTemplateDactilar,ScoreDactilar,TiempoDesalojarEsclusa,TiempoPermanenciaEsclusa,TiempoConsultaStatusEES,TiempoRegistroEES,TiempoObtencionBiometriaEES,TiempoVerificacionHuellaEES,CalidadH1) VALUES (%s);" % var_string
    return query_string


def create_data_table_calidad():
    return "CREATE TABLE IF NOT EXISTS `piloto_algeciras`.`calidad` (" \
           "`FechaInicio` VARCHAR(19)," \
           "`FechaFin` VARCHAR(19)," \
           "`Hash` VARCHAR(44)," \
           "`Instalacion` VARCHAR(11)," \
           "`ModuloIdentificacion` VARCHAR(11)," \
           "`TipoDocumento` VARCHAR(26)," \
           "`PaisEmisor` VARCHAR(3)," \
           "`Sexo` VARCHAR(11)," \
           "`Edad` INT," \
           "`TipoImagen` VARCHAR(17)," \
           "`BackgroundUniformity` INT," \
           "`DeviationFromFrontalPose` REAL," \
           "`DeviationFromUniformLighting` REAL," \
           "`Sharpness` REAL," \
           "`Exposure` REAL," \
           "`EyeDistance` REAL," \
           "`Glasses` REAL," \
           "`GrayScaleDensity` REAL," \
           "`Male` REAL," \
           "`MouthClosed` REAL," \
           "`Age` INT," \
           "`Crown` REAL," \
           "`Chin` REAL," \
           "`Eye0GazeFrontal` REAL," \
           "`Eye1GazeFrontal` REAL," \
           "`Eye0Open` REAL," \
           "`Eye1Open` REAL," \
           "`Eye0Red` REAL," \
           "`Eye1Red` REAL," \
           "`Eye0Tinted` REAL," \
           "`Eye1Tinted` REAL," \
           "`NatualSkinColour` REAL," \
           "`FaceConfidence` INT," \
           "`Eye0Confidence` REAL," \
           "`Eye1Confidence` REAL," \
           "`ISO_19794_5_EyesGazeFrontalBestPractice` INT," \
           "`ISO_19794_5_EyesNotRedBestPractice` INT," \
           "`ISO_19794_5_EyesOpenBestPractice` INT," \
           "`ISO_19794_5_GoodExposure` INT," \
           "`ISO_19794_5_GoodGrayScaleProfile` INT," \
           "`ISO_19794_5_GoodVerticalFacePosition` INT," \
           "`ISO_19794_5_HasNaturalSkinColour` INT," \
           "`ISO_19794_5_HorizontallyCenteredFace` INT," \
           "`ISO_19794_5_ImageWidthToHeightBestPractice` INT," \
           "`ISO_19794_5_IsBackgroundUniformBestPractice` INT," \
           "`ISO_19794_5_IsBestPractice` INT," \
           "`ISO_19794_5_IsCompliant` INT," \
           "`ISO_19794_5_IsFrontal` INT," \
           "`ISO_19794_5_IsFrontalBestPractice` INT," \
           "`ISO_19794_5_IsLightingUniform` INT," \
           "`ISO_19794_5_IsSharp` INT," \
           "`ISO_19794_5_LengthOfHead` INT," \
           "`ISO_19794_5_LengthOfHeadBestPractice` INT," \
           "`ISO_19794_5_MouthClosedBestPractice` INT," \
           "`ISO_19794_5_NoHotSpots` INT," \
           "`ISO_19794_5_NoTintedGlasses` INT," \
           "`ISO_19794_5_OnlyOneFaceVisible` INT," \
           "`ISO_19794_5_Resolution` INT," \
           "`ISO_19794_5_ResolutionBestPractice` INT," \
           "`ISO_19794_5_WidthOfHead` INT," \
           "`ISO_19794_5_WidthOfHeadBestPractice` INT);"


def generate_query_calidad():
    var_string = ', '.join(["%s"] * 61)
    query_string = "INSERT INTO `piloto_algeciras`.`calidad` (FechaInicio,FechaFin,Hash,Instalacion,ModuloIdentificacion,TipoDocumento,PaisEmisor,Sexo,Edad,TipoImagen,BackgroundUniformity,DeviationFromFrontalPose,DeviationFromUniformLighting,Sharpness,Exposure,EyeDistance,Glasses,GrayScaleDensity,Male,MouthClosed,Age,Crown,Chin,Eye0GazeFrontal,Eye1GazeFrontal,Eye0Open,Eye1Open,Eye0Red,Eye1Red,Eye0Tinted,Eye1Tinted,NatualSkinColour,FaceConfidence,Eye0Confidence,Eye1Confidence,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice) VALUES (%s);" % var_string
    return query_string
