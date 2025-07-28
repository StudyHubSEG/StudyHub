import time
from .Stats_Common import Stats_CommonTestCase
from .Stats_Common import (
    STUB_srteSensorConfigCliCreate,
    STUB_srteSensorConfigCliDelete,
)
from utilities.commonPredicates import checkTrue
from utilities.prereq import Prereq
import utilities.SR.Predicates as SR_Preds


class TEST_Stats_Spotlight_Sid(Stats_CommonTestCase):
    """
    SR Sid Spotlight.
    """

    def testSetup(self):
        super().testSetup()

        for d in self.ALL_DEVICES:
            d.stubEnable(STUB_srteSensorConfigCliCreate)
            d.stubEnable(STUB_srteSensorConfigCliDelete)

    def testExecute(self):
        algo0_labels = [16001, 16002, 16003]
        flex_labels = [17002, 17003, 18002, 18003, 19002, 19003]
        adj_labels = [32000, 32001]

        with self.testlog.step(
            "Enable spotlight+collection on algo0 range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in algo0_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "16000" "16999" stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Disable spotlight on algo0 range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in algo0_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "16000" "16999" stats-spotlight-state off"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Re-Enable spotlight on algo0 range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in algo0_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "16000" "16999" stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Remove the algo0 range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in algo0_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.sendConfig(
                """no segment-routing sid-stats-range "16000" "16999" """
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Enable spotlight+collection on flex range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in flex_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            # no labels alloc'ed for FA local, but stats still enabled
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "17000" "19999" stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Disable spotlight on flex range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in flex_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            # no labels alloc'ed for FA local, but stats still enabled
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "17000" "19999" stats-spotlight-state off"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Re-Enable spotlight on flex range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in flex_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            # no labels alloc'ed for FA local, but stats still enabled
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "17000" "19999" stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Remove the flex range",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in flex_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            # no labels alloc'ed for FA local, but stats still enabled
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.sendConfig(
                """no segment-routing sid-stats-range "17000" "19999" """
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Enable spotlight+collection on adjacency SID labels",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing adj-sid-stats stats-collection on stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Disable spotlight on adjacency SID labels",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.sendConfig(
                """segment-routing adj-sid-stats stats-spotlight-state off"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Re-Enable spotlight on adjacency SID labels",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing adj-sid-stats stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Remove adjacency SID spotlight configurations",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.sendConfig(
                """no segment-routing adj-sid-stats stats-spotlight-state"""
            )
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Re-Enable spotlight on adjacency SID labels and remove adjacency SID configurations",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing adj-sid-stats stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.sendConfig("""no segment-routing adj-sid-stats""")
            self.sanityCheck(devices=[self.UUT])

        with self.testlog.step(
            "Re-Enable spotlight on SIDs and remove segment-routing configurations",
            pass_on_exit=True,
            reraise_ex=True,
        ):
            # Re-enable spotlight on algo0 range
            for l in algo0_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "16000" "16999" stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])
            
            # Re-enable spotlight on flex range
            for l in flex_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            # no labels alloc'ed for FA local, but stats still enabled
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing sid-stats-range "17000" "19999" stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])
            
            # Re-enable spotlight on adjacency SID labels
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliCreate, f"0 1")
            self.UUT.sendConfig(
                """segment-routing adj-sid-stats stats-spotlight-state on"""
            )
            self.sanityCheck(devices=[self.UUT])
            
            # Now remove all segment-routing configurations - this should delete all sensors
            for l in algo0_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            for l in flex_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            # no labels alloc'ed for FA local, but stats still enabled
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            for l in adj_labels:
                self.UUT.stubExpect(STUB_srteSensorConfigCliDelete, f"0 1")
            
            self.UUT.sendConfig("""no segment-routing""")
            self.sanityCheck(devices=[self.UUT])

    def testCleanup(self):
        for d in self.ALL_DEVICES:
            d.stubDisable(STUB_srteSensorConfigCliCreate)
            d.stubDisable(STUB_srteSensorConfigCliDelete)

        super().testCleanup()