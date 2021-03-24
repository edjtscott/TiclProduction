import FWCore.ParameterSet.Config as cms
from RecoHGCal.TICL.TICLSeedingRegions_cff import ticlSeedingTrk

from TiclProduction.Configuration.myDUMMYiterations_cff import filteredLayerClustersALL1,filteredLayerClustersALL2,filteredLayerClustersALL3

ticlTrackstersTRK1 = cms.EDProducer(
    "TrackstersProducer",
    algo_verbosity = cms.int32(0),
    detector = cms.string('HGCAL'),
    eid_graph_path = cms.string('RecoHGCal/TICL/data/tf_models/energy_id_v0.pb'),
    eid_input_name = cms.string('input'),
    eid_min_cluster_energy = cms.double(1),
    eid_n_clusters = cms.int32(10),
    eid_n_layers = cms.int32(50),
    eid_output_name_energy = cms.string('output/regressed_energy'),
    eid_output_name_id = cms.string('output/id_probabilities'),
    energy_em_over_total_threshold = cms.double(0.0),
    etaLimitIncreaseWindow = cms.double(2.1),
    filter_on_categories = cms.vint32(),
    filtered_mask = cms.InputTag("filteredLayerClustersALL1","ALL1"),
    itername = cms.string('TRK1'),
    layer_clusters = cms.InputTag("hgcalLayerClusters"),
    layer_clusters_hfnose_tiles = cms.InputTag("ticlLayerTileHFNose"),
    layer_clusters_tiles = cms.InputTag("ticlLayerTileProducer"),
    max_delta_time = cms.double(-1.),
    max_longitudinal_sigmaPCA = cms.double(9999),
    max_missing_layers_in_trackster = cms.int32(1),
    max_out_in_hops = cms.int32(99),
    mightGet = cms.optional.untracked.vstring,
    min_cos_pointing = cms.double(0.798),
    min_cos_theta = cms.double(0.866),
    maxLayer_cospointing = cms.int32(999),
    maxLayer_costheta = cms.int32(999),
    min_layers_per_trackster = cms.int32(5),
    oneTracksterPerTrackSeed = cms.bool(True),
    original_mask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask"),
    out_in_dfs = cms.bool(True),
    pid_threshold = cms.double(-1.0),
    promoteEmptyRegionToTrackster = cms.bool(True),
    root_doublet_max_distance_from_seed_squared = cms.double(9999),
    seeding_regions = cms.InputTag("ticlSeedingTrk"),
    shower_start_max_layer = cms.int32(9999),
    skip_layers = cms.int32(3),
    time_layerclusters = cms.InputTag("hgcalLayerClusters","timeLayerCluster")
)

ticlTrackstersTRK2 = ticlTrackstersTRK1.clone()
ticlTrackstersTRK2.filtered_mask = cms.InputTag("filteredLayerClustersALL2","ALL2")
ticlTrackstersTRK2.itername = cms.string('TRK2')

ticlTrackstersTRK3 = ticlTrackstersTRK1.clone()
ticlTrackstersTRK3.filtered_mask = cms.InputTag("filteredLayerClustersALL3","ALL3")
ticlTrackstersTRK3.itername = cms.string('TRK3')



trk_task = cms.Task(
    ticlSeedingTrk,filteredLayerClustersALL1,ticlTrackstersTRK1,
    ticlSeedingTrk,filteredLayerClustersALL2,ticlTrackstersTRK2,
    ticlSeedingTrk,filteredLayerClustersALL3,ticlTrackstersTRK3
)
