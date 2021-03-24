import FWCore.ParameterSet.Config as cms

from SimCalorimetry.HGCalSimProducers.hgcHitAssociation_cfi import lcAssocByEnergyScoreProducer, scAssocByEnergyScoreProducer
from SimCalorimetry.HGCalAssociatorProducers.LCToCPAssociation_cfi import layerClusterCaloParticleAssociation as layerClusterCaloParticleAssociationProducer
from SimCalorimetry.HGCalAssociatorProducers.LCToSCAssociation_cfi import layerClusterSimClusterAssociation as layerClusterSimClusterAssociationProducer

from RecoHGCal.TICL.SimTracksters_cff import *

from RecoLocalCalo.HGCalRecProducers.hgcalRecHitMapProducer_cfi import hgcalRecHitMapProducer as _hgcalRecHitMapProducer

sim_task = cms.Task(
    _hgcalRecHitMapProducer,
    lcAssocByEnergyScoreProducer,
    layerClusterCaloParticleAssociationProducer,
    scAssocByEnergyScoreProducer,
    layerClusterSimClusterAssociationProducer,
    filteredLayerClustersSimTracksters,
    ticlSimTracksters
)

#sim_path_2 = cms.Path(
#    ticlSimTrackstersEM
#)
